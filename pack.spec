# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['run.pyw'],
    pathex=[],
    binaries=[],
    datas=[('foo\\bin\\dashboard','foo\\bin\\dashboard'),
           ('foo\\bin\\logs\.gitignore','foo\\bin\\logs'),
           ('foo\\bin\\resources\\GeoIP.dat','foo\\bin\\resources'),
           ('foo\\bin\\resources\\GeoSite.dat','foo\\bin\\resources'),
           ('foo\\bin\\resources\\country.mmdb','foo\\bin\\resources'),
           ('foo\\bin\\Clash-meta.xml','foo\\bin'),
           ('foo\\bin\\clash.exe','foo\\bin'),
           ('foo\\bin\\WinSW.exe','foo\\bin'),
           ('config.yaml.example','.'),
           ('img\\logo.ico','img'),
           ('config\\config.ini.example','config'),],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='CMFW_mini',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['img\\logo.ico'],
    uac_admin=True,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='run',
)
