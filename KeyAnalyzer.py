from pynput.keyboard import Key, Listener


class KeyAnalyzer(object):
    pressed_key = None

    @classmethod
    def on_press(cls, key):
        cls.pressed_key = key
        return key not in [Key.left, Key.right, Key.up]

    @classmethod
    def listen(cls):
        with Listener(on_press=cls.on_press) as listener:
            listener.join()
