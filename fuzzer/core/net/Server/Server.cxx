#include "./Server.h"

TargetServer::TargetServer(ServerInfo &&info) : info_{std::move(info)} {}