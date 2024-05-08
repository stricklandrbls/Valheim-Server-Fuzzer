#pragma once
#include <string>
struct ServerInfo
{
  std::string hostname;
  unsigned short port;
};

class TargetServer
{
public:
  TargetServer(ServerInfo &&);
  const std::string &hostname() const noexcept { return this->info_.hostname; }
  const unsigned short &port() const noexcept { return this->info_.port; }

private:
  ServerInfo info_;
};