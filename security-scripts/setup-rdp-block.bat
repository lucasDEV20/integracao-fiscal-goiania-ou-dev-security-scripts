@echo off
title Bloqueio de Seguranca RDP - Windows
echo [INFO] Iniciando configuracoes de endurecimento de rede...

:: Bloqueia conexoes remotas no Registro do Windows
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 1 /f

:: Desabilita a regra de entrada no Firewall para a porta 3389
netsh advfirewall firewall set rule group="remote desktop" new enable=No

echo [OK] Acesso remoto bloqueado e Firewall configurado.
pause