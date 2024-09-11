<h1 align="center">Bot para auxiliar pessoas com deficiência visual </h1>
<h2 align="center"> <i>Aurion</i></h2>

<h4 align="center"> <i>Avaliação final do programa de bolsas Compass UOL para formação em machine learning para AWS.</i></h4>

![Imagem|Compass](assets/banner.png)

## 🌐 Sobre o Projeto
<p align="justify"> 
Este bot será desenvolvido com o objetivo oferecer uma ferramenta inclusiva para pessoas cegas, inspirada no movimento <a href="https://mwpt.com.br/criadora-do-projeto-pracegover-incentiva-descricao-de-imagens-na-web/">#ParaCegoVer</a>, que incentiva a descrição de imagens na web. A iniciativa, criada por uma defensora da acessibilidade visual, tem como propósito tornar o conteúdo digital mais acessível para pessoas com deficiência visual, promovendo a inclusão e a equidade. Integrado ao Telegram, o bot permitirá que os usuários enviem imagens para receber descrições detalhadas em áudio ou texto.
</p>

<p align="justify">
O bot estará disponível publicamente no Telegram, onde os usuários poderão interagir de maneira simples e eficiente. Dessa forma, este bot ofecerá uma solução inclusiva e tecnológica para que pessoas cegas possam compreender o conteúdo de imagens de forma acessível. A combinação dos serviços AWS permitirá uma interação fluida e eficaz, com descrições em áudio de alta qualidade e uma experiência de usuário otimizada.
</p>

## 🏗️ Arquitetura do Projeto
![Imagem|Compass](assets/Arquitetura.png)

## 🚀 Como utilizar
No telegram, busque por ``Aurion, Seu assistente visual`` e inicie a conversa.

## 📂 Estrutura das Pastas
```bash
  📁 sprints-9-10-pb-aws-abril
  │
  ├── 📁 assets
  │   ├── Arquitetura.png
  │   └── banner.png
  │          
  ├── 📁 src
  │   │
  │   └── 📁 chatbot
  │   │   └── aurion.zip
  │   │
  │   ├── 📁 lambda
  │   │   ├── bedrock.py
  │   │   ├── dynamo.py
  │   │   ├── image_processing.py
  │   │   ├── lambda_function.py
  │   │   ├── lex_interaction.py
  │   │   ├── rekognition.py
  │   │   ├── telegram_interaction.py
  │   │   ├── textract.py
  │   │   └── transcribe.py
  │                                                    
  └── README.md                                 
```

## 💻 Tecnologias
- AWS Bedrock
- AWS Rekognition
- AWS Transcribe
- AWS S3
- AWS Lex
- AWS Textract
- API Gateway
- Telegram
- Python

## ❌ Dificuldades
- Dificuldades com análise de imagens:
  <p>Tivemos desafios significativos ao trabalhar com a análise de imagens utilizando o AWS Rekognition.</p>
 
- Labels inconsistentes:
  <p>O principal problema estava relacionado às labels inconsistentes fornecidas pelo serviço.</p>
 
- Resultados incorretos no AWS Bedrock:
  <p>As inconsistências nas labels resultaram em análises imprecisas, afetando a integração dos dados com o AWS Bedrock.</p>

## 👨‍💻 Autores
<div>
  <table style="margin: 0 auto;">
    <tr>
      <td><a href="https://github.com/GabrielAvelarbr"><img loading="lazy" src="https://avatars.githubusercontent.com/u/117688731?v=4" width="115"><br><sub>Gabriel Avelar</sub></a></td>
      <td><a href="https://github.com/JoseJaan"><img loading="lazy" src="https://avatars.githubusercontent.com/u/120669342?v=4" width="115"><br><sub>José Neto</sub></a></td>
      <td><a href="https://github.com/Layonj300"><img loading="lazy" src="https://avatars.githubusercontent.com/u/106559843?v=4" width="115"><br><sub>Layon Reis</sub></a></td>
      <td><a href="https://github.com/LuizFillipe1"><img loading="lazy" src="https://avatars.githubusercontent.com/u/78454639?v=4" width="115"><br><sub>Luiz Fillipe</sub></a></td>
      <td><a href="https://github.com/PamelaPavan"><img loading="lazy" src="https://avatars.githubusercontent.com/u/97994995?v=4" width="115"><br><sub>Pamela Pavan</sub></a></td>
    </tr>
  </table>
</div>
