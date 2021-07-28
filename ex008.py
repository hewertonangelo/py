largura = float(input('Largura da parede:'))
altura = float(input('Altura da parede:'))

print('Sua parede tem a dimensão de {}x{} e a sua área é de {}m².\n'
      'Para pintar essa parede, você precisará de {}l de tinta'
      .format(largura,altura,altura*largura,(altura*largura)/2))