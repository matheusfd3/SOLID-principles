# SOLID Principles

O **SOLID** é um acrônimo que representa um conjunto de cinco princípios de design de software que ajudam a criar sistemas mais fáceis de manter, entender e expandir. Esses princípios são amplamente utilizados no desenvolvimento de software orientado a objetos  e foram introduzidos por Robert J. Martin (Uncle Bob).

## S - Single Responsibility Principle (Princípio da Responsabilidade Única):

- Um módulo deve ter um, e apenas um, motivo para alteração.
- Um módulo deve ser especializado em um único assunto e possuir apenas uma única responsabilidade dentro do seu software.
- Um módulo é apenas um conjunto coeso de funções e estruturas de dados.

## O - Open/Closed Principle (Princípio Aberto/Fechado):

- Um artefato de software deve estar aberto para extensão, mas fechado para modificação.
- Em outras palavras, o comportamento de um artefato de software deve ser extensível, sem ter que modificar esse artefato.

## L - Liskov Substitution Principle (Princípio da Substituição de Liskov):

- Objetos podem ser substituídos por seus subtipos sem que isso afete a execução correta do programa.
- O LSP pode ser estendido ao nível da arquitetura. Uma simples violação de substituição, pode fazer com que a arquitetura de um sistema seja poluída com uma quantidade significativa de mecanismos extras.

## I - Interface Segregation Principle (Princípio da Segregação da Interface):

- Uma classe não deve ser forçada a implementar interfaces que ela não utiliza.
- Em vez disso, as interfaces devem ser segregadas em conjuntos menores e mais específicos de métodos.

## D - Dependency Inversion Principle (Princípio da Inversão de Dependência):

- Módulos de alto nível não devem depender diretamente dos módulos de baixo nível.
- O Princípio da Inversão de Dependência (DIP) nos diz que os sistemas mais flexíveis são aqueles em que as dependências do código-fonte referem-se apenas a abstrações, não concreções.