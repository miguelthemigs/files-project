# Projeto Hackatown do Arquivo Nacional - Viva Documentos
![Screenshot 2024-04-08 151719](https://github.com/miguelthemigs/files-project/assets/93150152/1fc45169-fcff-4b84-af0d-4bc7b615ef11)

## Visão Geral
Este projeto apresenta uma aplicação web interativa, desenvolvida em Django, desenvolvida para o Hackatown do Arquivo Nacional, com o objetivo de engajar a comunidade na descrição colaborativa de arquivos públicos. 
Usuários podem contribuir descrevendo títulos, datas, descrições detalhadas e tags para documentos que são apresentados de forma aleatória. Quanto mais descrições ele fornecer, mais o usuário ganha pontos e pode juntar emblemas.
Ele foi pensado e programado para funcionar de modo responsivo e compatível em todos os aparelhos que for rodar, sendo eles tablets, computadores ou celulares.
![image](https://github.com/miguelthemigs/files-project/assets/93150152/6c3277cd-cc77-4b02-bcf2-c60f901da3a2)

## Funcionalidades
- **Descrição Colaborativa**: Usuários podem inserir descrições para títulos, datas, descrições detalhadas e tags. Cada contribuição é votada pela comunidade e descrições com maior número de votos seriam iriam para análise, para oficializar.
  ### Títulos, descrições ou data (exemplo com título):
  ![image](https://github.com/miguelthemigs/files-project/assets/93150152/a6069d88-b59f-4896-86b3-721c06072030)
  ### Tags
  - Podemos concordar com tags escritas por outros usuários:
  ![image](https://github.com/miguelthemigs/files-project/assets/93150152/e4d30768-c6a4-4251-8afe-7ca0682c3457)
  - Ou nós mesmos escrevemos nossas próprias tags:
  ![image](https://github.com/miguelthemigs/files-project/assets/93150152/507e4ecb-5554-4145-96e9-680c20948953)
  - O vocabulário controlado (palavras padrões fornecidas pelo Arquivo) não foi implementado, porém é simples de fazer e de muito valor para o Arquivo Nacional, já segue o padrão das tags, basta colocar tags específicas.
    
- **Seleção Aleatória de Documentos**: Após a conclusão de uma descrição, um novo documento é apresentado aleatoriamente ao usuário, mantendo o engajamento e a variedade.
- **Sistema de Pontuação**: Contribuidores recebem pontos por cada elemento que descrevem. Pontos adicionais são concedidos quando uma palavra sugerida é altamente votada.
  
- **Emblemas de Reconhecimento**: Para incentivar a participação contínua, os usuários ganham emblemas ao atingir diferentes níveis de pontuação, que são exibidos na página do perfil.
  ![image](https://github.com/miguelthemigs/files-project/assets/93150152/cebc6c6c-fbd9-4bfe-b3d5-4de9247796bb)

- **Dashboard Analítico**: Uma dashboard para administradores e usuários avançados que mostra as palavras mais votadas em seus respectivos documentos, para facilitar a análise pelo Arquivo Nacional.
 ![image](https://github.com/miguelthemigs/files-project/assets/93150152/0b9e3223-2375-4a12-b18d-aaea23b1089c)

