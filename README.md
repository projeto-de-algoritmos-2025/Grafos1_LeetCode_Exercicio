# Grafos1_LeetCode_Exercício
**Número da Lista**: 1<br>
**Conteúdo da Disciplina**: Grafos 1 <br>
## Alunos
|Matrícula | Aluno |
| -- | -- |
| 22/2006383 | Rafael Melo Matuda |
| 22/1021868 | Caio Falcão Habibi Costa |
## Sobre
Para explorar o conteúdo do tópico de Grafos 1, a dupla escolheu quatro
exercícios na plataforma online LeetCode: dois de nível difícil e dois
de nível médio, para igualar o trabalho de cada um dos membros.
## Screenshots
### [329(Difícil)](https://leetcode.com/problems/longest-increasing-path-in-a-matrix)
Modelei a matriz como um grafo e usei DFS para buscar caminhos
crescentes. Para otimizar, utilizei memoização para guardar o tamanho
do maior caminho a partir de cada célula já vista. A DFS visita cada
nó, explora vizinhos maiores e retorna o maior caminho, usando valores
memoizados. O resultado é o máximo dos caminhos encontrados pela DFS
iniciada em cada célula.
![PrintResolucao329](/Grafos1_LeetCode_Exercicio/assets/329img.png)<br>
https://www.youtube.com/watch?v=o51kJ3xiWRM
## Screenshots
### [797(Médio)](https://leetcode.com/problems/all-paths-from-source-to-target)
Modelei o grafo dado e usei DFS para encontrar todos os caminhos do nó
inicial ao nó final. A DFS explora cada nó, segue para os vizinhos e
guarda cada caminho completo encontrado. O resultado é a lista de todos
os caminhos válidos do início ao fim do grafo
![PrintResolucao797](/Grafos1_LeetCode_Exercicio/assets/797img.png)<br>
https://www.youtube.com/watch?v=KaMLwiLbfG4
### [2360(Difícil)](https://leetcode.com/problems/longest-cycle-in-a-graph)
![PrintResolucao2360](/Grafos1_LeetCode_Exercicio/assets/2360img.jpg)
https://www.youtube.com/watch?v=LOkl3O_z8ko
### [785 (Médio)](https://leetcode.com/problems/is-graph-bipartite)
![PrintResolucao2360](/Grafos1_LeetCode_Exercicio/assets/785img.png)<br>
https://www.youtube.com/watch?v=A6-DgQbq6Ek
## Instalação
**Linguagem**: Python<br>
## Uso
Explique como usar seu projeto caso haja algum passo a passo após o
comando de execução.
## Outros