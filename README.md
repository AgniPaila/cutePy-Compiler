# 🐍 cutePy-compiler

A Python-based compiler for **cutePy**, a Python-like programming language.  
This project compiles cutePy code into **RISC-V assembly**, using multiple intermediate stages.

## 📖 Description

The **cutePy-compiler** translates `.cpy` source files written in the **cutePy** language into executable **RISC-V assembly code**. 

## 🧱 Compiler Pipeline Overview
- Lexical Analysis
- Syntax Analysis
- Intermediate Code
- Symbol Table
- Final Code (Assembly) 

Each stage is designed to be extensible, allowing future enhancements such as optimization passes or backend code generators for additional architectures.

## 🚀 Getting Started

### ✅ Requirements

- Python **3.10** or higher
- RISC-V simulator (optional, for testing output)

### 🛠️ How to Compile a cutePy Program

1. Clone the repository
2. Run: python3 cutePy.py path/to/your_program.cpy
3. The final RISC-V assembly output will be saved in the .asm file
4. Intermediate representations (.int, .symb files) will be generated and saved, providing visibility into the compilation pipeline

## 📘 Course Info
Course: Μεταφραστές (Compilers)

Team: This project was developed in collaboration with one fellow student.
