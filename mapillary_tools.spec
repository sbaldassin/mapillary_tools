# -*- mode: python -*-

block_cipher = None

options = [('u', None, 'OPTION')]

a = Analysis(['bin/mapillary_tools'],
             pathex=[SPECPATH],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['./pyinstaller/hooks'],
             runtime_hooks=['./pyinstaller/runtime-hooks/ssl.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          options,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='mapillary_tools',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
