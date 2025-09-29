
# Chatbot simples com dicionário

respostas = {
    "iae, de boa?": "aoouba, de boa!",
    "tudo bem?": "Suave, e você?",
    "qual é o seu nome?": "Meu nome é Vitu e fui criado pra responder pergunta né!",
    "vitu?": "Vitu mamando kkkkkkkk parei, foi mal!",
    "o que você faz?": "Eu respondo perguntas!",
    "aí sim, brabão!": "É filhão, vai achando!",
    "então quem é Goat, Jordan ou LeBron?": "Jordan né mané, mas o Lebronha é o melhor jogador, sem dúvidas!",
    "quem é melhor, Messi ou Cristiano Ronaldo?": "Messi!",
    "agora quem é o maior, Pelé ou Maradona?": "Pô, Pelé catou a xuxa mano, o cara tem 3 copas, é o rei do futebol!",
    "seu eu comer leite com manga eu vou morrer ou não?": "Provavelmente!",
    "em que ano vai acontecer o meu primeiro bilhão?": "kkkkkkkkkkkkkk aham",
    "tu acha que eu sou corno?": "Manda foto da cara pra gente ver um negócio aqui, rapidão!",
    "será que a annita e o kaka dariam certo?": "minha inteligência vai só até essa pergunta!",
    "nike ou adidas?": "Nike né pai!",
    "em uma mão eu tenho sydney sweeney, na outra margot robbie. Quem você escolhe?": "put your hands together neguinho!",
    "os títulos do kevin durant são dignos?": "Hell nah",
    "ou, vlw demais slk, tmj!": "Nada não meu rei, é nozes!",
    "vlw": "Vlw flw!!"
}

while True:
    pergunta = input("Você: ").lower()  # transforma tudo que o usuário digitar em minúsculo
    
    if pergunta == "sair":
        print("Chatbot: Vlw flw! 👋")
        break

    resposta = respostas.get(pergunta, "Tendi foi nada! Ou tu pergunta de outro jeito ou faz outra pergunta!")
    print(f"Chatbot: {resposta}")
