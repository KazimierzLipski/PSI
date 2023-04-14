#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/socket.h>

int main(int argc, char **argv)
{
  char bufor[10000];
  int port;
  if (argc < 2) {
    port = 8000;
    printf("Brak podanego portu\nProgram będzie korzystał z portu 8000\n");
  }
  else {
    port = (int)strtol(argv[1], NULL, 0);
    printf("Korzystamy z portu %d\n", port);
  }
  struct sockaddr_in adres_serwera = {
      .sin_family = AF_INET,
      .sin_addr.s_addr = htonl(INADDR_ANY),
      .sin_port = htons(port)
  };
  struct sockaddr_in adres_klienta;
  socklen_t dlugosc_adresu_klienta = sizeof(adres_klienta);
  int gniazdko = socket(AF_INET, SOCK_DGRAM, 0);
  if (gniazdko < 0) {
    perror("Błąd przy tworzeniu gniazdka");
    return 1;
  }
  if (bind(gniazdko, (const struct sockaddr *)&adres_serwera, sizeof(adres_klienta)) < 0) {
    perror("Błąd przy wiązaniu gniazdka");
    return 1;
  }
  printf("Uruchomiono prawidłowo\n");
  while (1) {
    int wiadomosc_otrzymana = (int)recvfrom( gniazdko, bufor, sizeof(bufor), 0, (struct sockaddr *)&adres_klienta, &dlugosc_adresu_klienta);
    if (wiadomosc_otrzymana < 0) {
      perror("Błąd w otrzymanych danych");
      return 1;
    }
    printf("Otrzymano %d bajtów danych z %s:\n%.*s\n\n", wiadomosc_otrzymana, inet_ntoa(adres_klienta.sin_addr), wiadomosc_otrzymana, bufor);
  }
  return 0;
}