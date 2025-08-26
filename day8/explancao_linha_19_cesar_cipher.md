Intuição simples

Pensa no relógio:

Se agora são 22h e você somar 5 horas → 22 + 5 = 27.

Mas no relógio só existem 24 horas.

Então você "dá a volta" → 27 % 24 = 3.
Ou seja, 27h no relógio é 3h.

O alfabeto funciona igual: só existem 26 posições (de 0 até 25).
O % 26 faz o índice "voltar para o começo" quando passa de 25.

Explicação matemática

O operador módulo pega o resto da divisão.

👉 Exemplo: 29 % 26

29 dividido por 26 → cabe 1 vez (1 × 26 = 26).

Sobra 3.

O resto é 3 → por isso 29 % 26 = 3.

Então, sempre que você passa do limite (25), o % "joga fora as voltas completas" e deixa só o ponto onde parou dentro do intervalo válido (0–25).

Por que isso é a "volta"

O alfabeto é como uma roda com 26 casas.

Cada vez que você soma um número ao índice, anda casas na roda.

O % 26 descarta quantas voltas completas você deu na roda, e fica só com a posição final.

Sem %:

Índice 29 seria "fora da roda" (erro no Python).

Com %:

Índice 29 → vira 3 → você volta pro começo e continua contando.

👉 Em resumo: o que faz dar a volta é o cálculo do resto (%), porque ele garante que o número nunca passe do tamanho da lista (26 letras).

---

Se o valor não passa de 25, ou seja, ainda está dentro do intervalo válido (0 até 25), o operador % não muda nada.

Por quê?

Exemplo:

posicao_deslocada = 10
10 % 26 = 10 → continua sendo 10.

Porque 10 dividido por 26 dá 0 voltas completas e sobra 10.
O resto é o próprio número.

Em outras palavras:

Quando está dentro do limite (0–25), o % não faz nada.
Quando passa de 25 (ou fica negativo), o % corrige automaticamente, trazendo de volta pro intervalo válido.

🔑 É por isso que o % len(alphabet) é uma "garantia":

Se está no intervalo → mantém. Se sai do intervalo → ajusta.
