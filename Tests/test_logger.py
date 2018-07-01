from datetime import datetime
import Tagcounter.logger as logger

urls_EC0 = ("", "yandex.ru", "1")


def test_log(tmpdir):
    """Test checks whether logger saves data in file in normal case"""

    for url in urls_EC0:
        file = tmpdir.join("test_log.txt")
        date = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
        logger.log(file.strpath, url)
        assert "{} {}\n".format(date, url) == file.readlines()[-1]
