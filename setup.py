from distutils.core import setup
import os, sys, glob

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name="Bus-Reminder",
      scripts=['Bus-Reminder'],
      version='0.1.0',
      maintainer="Juha Autero",
      maintainer_email="email@example.com",
      description="A PySide example",
      long_description=read('Bus-Reminder.longdesc'),
      data_files=[('share/applications',['Bus-Reminder.desktop']),
                  ('share/icons/hicolor/64x64/apps', ['Bus-Reminder.png']),
                  ('share/Bus-Reminder/qml', glob.glob('qml/*.qml')), ],)
