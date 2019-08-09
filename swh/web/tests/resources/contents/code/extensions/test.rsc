# Берем список DNS серверов из /ip dns
 # Проверяем их доступность,
# и только рабочие прописываем в настройки DHCP сервера
:global ActiveDNSServers []
:local PingResult 0
:foreach serv in=[/ip dns get servers] do={
  :do {:set PingResult [ping $serv count=3]} on-error={:set PingResult 0}
  :if ($PingResult=3) do={ :set ActiveDNSServers ($ActiveDNSServers,$serv) }
# отладочный вывод в журнал
  :log info "Server: $serv, Ping-result: $PingResult";
}

/ip dhcp-server network set [find address=192.168.254.0/24] dns-server=$ActiveDNSServers

#---   FIX TTL  ----
/ip firewall mangle chain=postrouting action=change-ttl new-ttl=set:128 comment="NAT hide"
