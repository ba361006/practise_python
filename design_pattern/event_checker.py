import re
from datetime import datetime
from time import sleep
from types import TracebackType
from typing import List, Optional, Type

import pytz
from restbuilder.base import REST_API


class EventChecker:
    def __init__(self, rest_client: REST_API):
        self.rest_client = rest_client
        self.expected_events: List[str] = []
        self.matched_events: List[str] = []
        self.started_at: Optional[datetime] = None
        self.timeout: int = 2

    def __call__(self, expected_events: List[str], timeout: int = 2) -> "EventChecker":
        self.expected_events = expected_events
        self.timeout = timeout
        return self

    def __enter__(self) -> "EventChecker":
        self.started_at = datetime.now(tz=pytz.utc).replace(tzinfo=None)
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        if exc_value is not None:
            raise exc_value
        for _ in range(self.timeout * 10):
            if self._check_expected_events_exists():
                break
            sleep(0.1)
        else:
            raise TimeoutError(
                f"Timed out waiting for events {self.expected_events}, found {self.matched_events}"
            )

    def _check_expected_events_exists(self) -> bool:
        response = self.rest_client.api("v1").get(
            f"events?created_at_after={self.started_at.isoformat()}"
        )
        assert self.rest_client.last_status() == 200, str(response)

        all_events = [event["description"] for event in response["items"]]

        matched_events: List[str] = []
        for expected_event in self.expected_events:
            matched_event = self._check_event_match(
                expected_event=expected_event, events=all_events
            )
            if not matched_event:
                return False
            all_events.pop(all_events.index(matched_event))
            matched_events.append(matched_event)
        self.matched_events = matched_events
        return True

    @staticmethod
    def _check_event_match(expected_event: str, events: List[str]) -> Optional[str]:
        for event in events:
            if re.match(expected_event, event):
                return event
        return None
