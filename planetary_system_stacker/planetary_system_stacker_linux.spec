# -*- mode: python -*-

block_cipher = None

# Integrate astropy as data directory instead of module:
import astropy
astropy_path, = astropy.__path__

a = Analysis(['planetary_system_stacker.py'],
             pathex=['/home/rolf/Pycharm-Projects/PlanetarySystemStacker/planetary_system_stacker'],
             binaries=[],
             datas=[('/home/rolf/Pycharm-Projects/PlanetarySystemStacker/Documentation/Icon/PSS-Icon-64.jpg', '.' ),
             ('/home/rolf/Pycharm-Projects/PlanetarySystemStacker/Documentation/PlanetarySystemStacker_User-Guide.pdf', '.' ),
             ('/home/rolf/Pycharm-Projects/PlanetarySystemStacker/planetary_system_stacker/Videos/*', 'Videos' ),
             (astropy_path, 'astropy')],
             hiddenimports=['pywt._extensions._cwt', 'scipy._lib.messagestream', 'shelve', 'csv'],  # The last two required by astropy
             hookspath=[],
             runtime_hooks=[],
             excludes=['astropy'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='planetary_system_stacker',
          debug=False,
          strip=False,
          upx=True,
          console=False )   # To display a console window, change value to True.
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='PlanetarySystemStacker')
