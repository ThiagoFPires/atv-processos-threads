# Atividade Prática: Processos e Threads em Python

Este projeto consiste na implementação, medição e análise comparativa de desempenho entre execução **sequencial**, **com múltiplos processos** e **com múltiplas threads** em Python (CPython), aplicando o algoritmo de identificação e contagem de números primos no intervalo de **2 até 200.000**.

Trabalho desenvolvido para a disciplina de **Computação Paralela e Distribuída**.

---

## 📋 Pré-requisitos

* **Python 3.10** ou superior instalado (testado e homologado no Python 3.14).
* Sistema Operacional: Windows 10/11 ou Linux.
* **Nenhuma biblioteca externa é necessária** para rodar os algoritmos de cálculo (utiliza apenas os módulos nativos `time`, `multiprocessing` e `threading` da biblioteca padrão do Python).

---

## ⚙️ Configuração do Ambiente

### 1. Verificar a instalação do Python
Abra o terminal (PowerShell, CMD ou Bash) e certifique-se de que o Python está configurado no seu `PATH`:

```bash
python --version
```
> Caso utilize Windows e o comando não seja reconhecido, utilize `py --version`.

### 2. (Opcional) Criação de Ambiente Virtual
Caso deseje isolar a execução em um ambiente virtual:

```bash
# Criar o ambiente virtual
python -m venv venv

# Ativar no Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Ativar no Linux / macOS
source venv/bin/activate
```

---

## 🚀 Como Executar

Cada estratégia possui seu próprio arquivo executável autônomo. No terminal, dentro da pasta do projeto, execute:

### 1. Execução Sequencial (Fluxo Único)
Executa a verificação de todos os números de 2 até 200.000 sequencialmente:
```bash
python sequencial.py
```
* **Saída esperada:** Quantidade total de primos encontrados (`17984`) e o tempo de execução em segundos.

### 2. Execução com Múltiplos Processos (Paralelismo Real)
Divide o intervalo em 4 blocos contíguos de 50.000 números, processados por 4 processos independentes via `multiprocessing.Process` comunicando-se via `Queue`:
```bash
python processos.py
```
* **Vantagem:** Cada processo possui sua própria instância do Python e seu próprio GIL, permitindo uso real de múltiplos núcleos da CPU.

### 3. Execução com Múltiplas Threads (Concorrência)
Divide o intervalo em 4 fatias executadas concorrentemente via `threading.Thread`:
```bash
python threads.py
```
* **Observação:** Em tarefas estritamente de CPU (*CPU-bound*), o Global Interpreter Lock (GIL) do CPython serializa as threads em um único núcleo físico, não produzindo aceleração sobre o sequencial.

---

## 📁 Estrutura de Arquivos

```text
├── sequencial.py                     # Implementação sequencial de referência
├── processos.py                      # Implementação paralela com 4 processos (multiprocessing)
├── threads.py                        # Implementação concorrente com 4 threads (threading)
├── resultados.json                   # Dados experimentais coletados (1, 2, 4 e 8 fluxos + hardware)
├── Relatorio_Processos_e_Threads.docx # Relatório técnico completo formatado nas normas ABNT
├── Relatorio_Processos_e_Threads.pdf  # Versão em PDF do relatório final
└── README.md                         # Este guia de configuração e uso
```

---

## 🖥️ Configuração da Máquina de Testes (Referência)

Os resultados do experimento documentados no relatório foram coletados no seguinte ambiente de hardware:

* **Processador:** AMD Ryzen 7 5700X (8 núcleos físicos / 16 threads, até 4.6 GHz, microarquitetura Zen 3)
* **Memória RAM:** 32 GB DDR4
* **Sistema Operacional:** Windows 11 Pro (x64)
* **Interpretador:** CPython 3.14 (64-bit)

---

## 📊 Síntese dos Resultados

| Abordagem | Fluxos | Tempo Médio | Speedup | Comportamento Principal |
| :--- | :---: | :---: | :---: | :--- |
| **Sequencial** | 1 | 0,1945 s | 1,00x | Base de comparação (1 núcleo a 100%) |
| **Processos** | 4 | 0,1940 s | 1,00x | Paralelismo real nos núcleos físicos |
| **Processos** | 8 | 0,2064 s | 0,94x | Estabilização por overhead de `spawn` e IPC |
| **Threads** | 4 | 0,2047 s | 0,95x | Estagnação de desempenho causada pela trava do GIL |

Para a análise aprofundada, gráficos comparativos e fundamentação teórica sobre Amdahl, GIL e IPC, consulte o [Relatório em PDF](Relatorio_Processos_e_Threads.pdf) ou [Word](Relatorio_Processos_e_Threads.docx).
