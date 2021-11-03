# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

datafiles =[('ale_c.dll', '.'),("ale_c.dll", "//PycharmProjects//pythonProject"), ("atari_py/ale_interface/ale_c.dll", "atari_py/ale_interface"), ("ChatBot.json", ".")]

a = Analysis(['TextEditor.py'],
             pathex=['//PycharmProjects//pythonProject', '/atari_py', 'atari_py', '.', "atari_py/ale_interface", "atari_py/ale_interface/","atari_py/atari_roms"],
             binaries=[("atari_py/atari_roms", "atari_py/atari_roms"), ("atari_py/tests", "atari_py/tests")],
             datas=datafiles,
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
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
          name='TextEditor',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
