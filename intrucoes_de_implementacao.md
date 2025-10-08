# 📋 Instruções de Implementação - Sistema de Questões Não Pontuadas

## ✨ O que foi implementado

O sistema agora suporta simulados com **65 questões**, onde **15 são aleatoriamente não pontuadas** a cada nova tentativa. As principais mudanças incluem:

1. ✅ Seleção aleatória de 15 questões não pontuadas no **início** de cada simulado
2. ✅ Indicador visual mostrando se a questão é pontuada ou não
3. ✅ Cálculo de pontuação considerando apenas as 50 questões pontuadas
4. ✅ Mensagem na explicação informando se a questão não é pontuada

---

## 📂 Arquivos Modificados

### 1. **dados/simulado_logica.py** ⭐ NOVO
Substitua o conteúdo completo do arquivo pelo código fornecido no artifact **"simulado_logica.py - Atualizado com questões não pontuadas"**.

**Principais funções adicionadas:**
- `gerar_questoes_nao_pontuadas()` - Gera aleatoriamente as 15 questões não pontuadas
- `calcular_pontuacao()` - Atualizada para considerar apenas questões pontuadas

---

### 2. **app.py** ⭐ ATUALIZADO
Substitua o conteúdo completo do arquivo pelo código fornecido no artifact **"app.py - Atualizado com questões não pontuadas"**.

**Principais mudanças:**
- Importação da nova função `gerar_questoes_nao_pontuadas`
- Geração das questões não pontuadas ao iniciar o simulado
- Armazenamento da lista de questões não pontuadas na sessão
- Passagem da informação `questao_pontuada` para os templates
- Cálculo final considerando apenas questões pontuadas

---

### 3. **templates/fazer_simulado.html** ⭐ NOVO DESIGN
Substitua pelo código do artifact **"fazer_simulado.html - Com indicador de questão pontuada"**.

**Novidades:**
- Badge verde "PONTUADA" ou cinza "NÃO PONTUADA" no canto superior esquerdo
- Visual limpo e informativo

---

### 4. **templates/explicacao.html** ⭐ NOVO (se não existe)
Crie este arquivo com o código do artifact **"explicacao.html - Com indicador de questão pontuada"**.

**Recursos:**
- Mostra se você acertou ou errou
- Exibe sua resposta e a resposta correta
- Mostra explicação (se disponível)
- Informa se a questão é pontuada
- Badge visual indicando status da questão

---

## 🎯 Como Funciona

### Fluxo do Sistema:

1. **Início do Simulado:**
   - Sistema carrega todas as questões
   - Embaralha as questões e opções
   - **Gera aleatoriamente 15 questões não pontuadas**
   - Salva tudo na sessão do usuário

2. **Durante o Simulado:**
   - Badge mostra se a questão atual é pontuada
   - Usuário responde normalmente
   - Sistema verifica resposta independente de ser pontuada

3. **Na Explicação:**
   - Mostra acerto/erro
   - Exibe explicação
   - Informa se a questão não é pontuada

4. **Resultado Final:**
   - Calcula pontuação **apenas** com as 50 questões pontuadas
   - Salva no banco de dados
   - Exibe percentual baseado em 50 questões

---

## 🔧 Para Usar com 65 Questões

Se você ainda tem apenas 3 questões nos seus simulados de teste, o sistema **já está preparado**. Quando você adicionar 65 questões:

```python
# Em dados/simulado_1.py (exemplo)
DADOS_SIMULADO = {
    "id": 1,
    "titulo": "Simulado Completo AWS",
    "questoes": [
        # ... adicione suas 65 questões aqui
        {
            "pergunta": "Sua pergunta aqui?",
            "opcoes": ["Opção A", "Opção B", "Opção C", "Opção D"],
            "resposta_correta": "Opção A",
            "explicacao": "Explicação detalhada aqui"
        },
        # ... até completar 65 questões
    ]
}
```

---

## ⚙️ Ajustar Quantidade de Questões Não Pontuadas

Para mudar a quantidade de questões não pontuadas (atualmente 15), edite esta linha no **app.py**:

```python
# Linha ~180 aproximadamente
questoes_nao_pontuadas = gerar_questoes_nao_pontuadas(total_questoes, 15)
                                                                      ↑
                                                            Mude este número
```

---

## ✅ Checklist de Implementação

- [ ] Substituir **dados/simulado_logica.py**
- [ ] Substituir **app.py**
- [ ] Substituir **templates/fazer_simulado.html**
- [ ] Criar/substituir **templates/explicacao.html**
- [ ] Testar com simulado de 3 questões
- [ ] Adicionar suas 65 questões reais
- [ ] Testar resultado final

---

## 🚀 Testando

1. Inicie o servidor: `python app.py`
2. Acesse um simulado
3. Observe o badge **"PONTUADA"** ou **"NÃO PONTUADA"**
4. Complete o simulado
5. Verifique que o resultado considera apenas as pontuadas

---

## 💡 Dicas

- As 15 questões não pontuadas são **diferentes** a cada novo simulado
- Se quiser ver quais questões não são pontuadas (para debug), adicione um print no código
- O sistema funciona com qualquer quantidade de questões (3, 10, 65, etc)
- A explicação só aparece se você adicionar o campo `"explicacao"` nas questões

---

## ❓ Dúvidas Comuns

**P: As questões não pontuadas mudam a cada tentativa?**
R: Sim! Cada vez que você **inicia** um novo simulado, 15 novas questões aleatórias serão não pontuadas.

**P: Posso ver quais questões não são pontuadas antes de responder?**
R: Sim! O badge aparece **durante** a resposta da questão.

**P: O banco de dados salva quais questões não foram pontuadas?**
R: Não, apenas o resultado final (acertos/50). A lista de não pontuadas existe apenas durante o simulado.

**P: Funciona com questões de múltipla escolha (checkbox)?**
R: Sim! O sistema já suporta questões com múltiplas respostas corretas.

---

## 📞 Suporte

Se tiver alguma dúvida durante a implementação, é só me chamar! 🚀