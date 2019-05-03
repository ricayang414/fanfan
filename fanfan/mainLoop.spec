# -*- mode: python -*-

block_cipher = None


a = Analysis(['mainLoop.py'],
             pathex=['appointmentInfo.py', 'dateSelection.py', 'frames.py', 'main.py', 'restaurant.py', 'selectRestaurant.py', 'signup.py', 'sub.py', 'timeInfo.py', 'userInformation.py', 'utility.py', 'C:\\Users\\willi\\fanfan'],
             binaries=[],
             datas=[],
             hiddenimports=['appointmentInfo', 'dateSelection', 'frames', 'main', 'restaurant', 'selectRestaurant', 'signup', 'sub', 'timeInfo', 'userInformation', 'utility'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='mainLoop',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='fanfan.ico')
