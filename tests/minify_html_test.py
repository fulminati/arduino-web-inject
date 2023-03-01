
from arduino_web_inject.pippo import cavallo

def test_inject_as_string():
    value = inject_as_string('tests/fixtures/index.html', '')
    print("VAL" + value)
    assert True

if __name__ == '__main__':
    test_inject_as_string()