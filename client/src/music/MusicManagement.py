import time


class MusicManagement():
    stop = False

    def run(self):
        while not self.stop:
            print("Playing music")
            self.music()

    def stop_music(self):
        self.stop = True
        print("Stopping music")

    def music(self):
        time.sleep(130)
