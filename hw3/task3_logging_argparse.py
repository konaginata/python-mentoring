import importlib
import logging
import argparse
from task2_importlib import get_package_path


def get_path_with_logging(package_name, c_level, f_level):
    console_handler = logging.StreamHandler()
    console_handler.setLevel(c_level)
    console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)

    file_handler = logging.FileHandler("package_info.log")
    file_handler.setLevel(f_level)
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)

    logger = logging.getLogger(__name__)
    result = get_package_path(package_name)

    if result != "Package not found":
        package = importlib.import_module(package_name)
        logger.warning("Package name: %s" % package_name)
        logger.warning("Package description: %s" % package.__doc__)
        logger.info("Package path: %s" % result)
        try:
            logger.debug("Package version: %s" % package.__version__)
        except AttributeError:
            logger.error("Package version not found")
    else:
        logger.error(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get package information')
    parser.add_argument('package', help='Package name')
    parser.add_argument('--console_level', default='DEBUG',
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], help='Console logging level')
    parser.add_argument('--file_level', default='DEBUG',
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], help='File logging level')
    args = parser.parse_args()

    console_level = getattr(logging, args.console_level)
    file_level = getattr(logging, args.file_level)
    get_path_with_logging(args.package, console_level, file_level)
