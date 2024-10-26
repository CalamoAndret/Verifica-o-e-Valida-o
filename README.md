### Fase Red

O objetivo inicial da fase Red foi definir o comportamento esperado da função `calcular_media`, incluindo uma série de testes que abrangem diferentes cenários. Esses cenários cobrem o cálculo da média com notas comuns, o caso onde todas as notas são zero, todas as notas são os valores máximos, valores decimais, e também casos inválidos, como notas fora do intervalo permitido (0 a 10) e entradas não numéricas. Como a função `calcular_media` ainda não foi implementada, a falha em todos os testes foi o resultado esperado, confirmando que os testes estavam configurados corretamente para identificar os requisitos necessários.

### Fase Green

Na fase Green, a implementação da função `calcular_media` foi feita de forma básica, assegurando que passasse nos testes iniciais sem validações complexas. Essa fase se concentrou em fazer a função passar nos testes básicos, realizando o cálculo da média das três notas. Com a execução dos testes novamente após a implementação, todos passaram com sucesso, o que validou que a lógica essencial de cálculo estava correta.

### Fase de Refatoração

A fase de Refatoração aprimorou a função `calcular_media` para torná-la mais robusta e segura para entradas diversas. Foram incluídas verificações adicionais para garantir que todas as notas fossem números válidos (inteiros ou decimais), que estivessem dentro do intervalo permitido (0 a 10) e que a média fosse arredondada para duas casas decimais, trazendo maior precisão e consistência à saída. Após esses aprimoramentos, os testes foram executados novamente para confirmar que a função continuava apresentando o comportamento correto e passando em todos os cenários de teste.