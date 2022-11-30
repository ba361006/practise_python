# Logger with fileconfig
The configuration file format understood by fileConfig() is based on configparser functionality.
The file must contain sections called `[loggers]`, `[handlers]` and `[formatters]` which identify by name the entities of each type which are defined in the file.

For each such entity, there is a separate section which identifies how that entity is configured. Thus, for a logger named `log01` in the `[loggers]` section, the relevant configuration details are held in a section `[logger_log01]`, and so do the `[handlers]` and `[formatters]`.

The root logger configuration must be specified in a section called [logger_root].


## logger.ini instructions
- [loggers]:
    - define loggers' name
- [handlers]
    - define handlers' name
- [formatters]
    - define formatters' name
- [logger_root]
    > Note: you can get root logger via `logging.getLogger(name="")` or just `logging`
    - level
        - define logging level for root logger
    - handlers
        - define handlers for root logger
- [logger_<custom_logger's_name>]
    > Note: qualname is needed for every logger except root logger
    - level
        - define logging level for this logger, if this entry is specified as `NOTSET`, the system consults loggers higher up the hierarchy to determine the effective level of the logger
    - handers
        - define handlers for this logger
    - qualname
        - this entry is the hierarchical channel name of the logger, that is to say the name used by the application to get the logger

- [handler_<custom_handler's_name>]
    > Note: Three of the entries are needed but can be blank
    - level
        - it logs everything if this entry has not been set or set as `NOTSET`
    - class
        - define handler's class in the `logging` package's namespace
        - handlers's name could also be written as `handlers.HTTPHandler` or sort
    - formatter
        - set the key name listed under `[formatters]`
    - args
        - refer to the constructors for the relevant handlers, it defaults to () if not provided

- [formatter_<custom_formatter's_name>]
    - format
        - define the overall format seting
    - datefmt
        - this entry is the strftime() - compatible date/time format string

## Note:
current setting is for running this file via vscode function `Run Python File`.

if running this file via vscode function `Run Python File`
it indicates that the root directory would be the same as where you run the .py file
`__name__` should be taken care of  since it return a directory with dot-notation started from the root directory.
To let every logger inherit to the custom logger, we should either
1. set every module/package name to qualname under logger.ini
2. create an ancestor logger like [with_code](/logging_practise/with_code/handler/logging.py) do
3. run .py file with command line, so the root directory will change and modify qualname to the root directory


if running this file via comamnd line -> python -m logging_practise.with_file.src.main
it indicates that the root directory would be the same as where you open the folder via vscode
thus, you might get ModuleNotFoundError.
It can be solved this, for example, your open practise_python folder via vscode
1. replace `from bar import bar` with `from logging_practise.with_file.src.bar import bar`, etc.
2. change the qualname under [logger_src] to from src to logging_practise