print("                   == LOCADORA S.A. ==")
d = int(input("Digite a quantidade de dias em que o veículo foi utilizado: "))
s = float(input("Certo, agora nos informe a distância (Km) total percorrida: "))
print(f"O serviço de locação do veículo por {d} dias e seu uso em {s:.2f} km,"
      f" ficou no total de R$ {60*d + 0.15*s:.2f}.\n              Agradecemos a preferência :)")
