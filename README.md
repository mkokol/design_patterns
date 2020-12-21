# Practicing design patterns with python

Practicing design patterns from a book: "Design Patterns, Elements of Reusable Object-Oriented Software" 

## Details

This project has the next design patterns:

  - Creational Patterns:
    - Abstract Factory
    - Builder
    - Factory Method
    - Prototype
    - Singleton
  - Structural Patterns:
    - Adapter
    - Bridge
    - Composite

### Requirements

* python3.7.3

### Installing

Configure the virtual environment for the project:

    python3 -m venv ./venv

Switch to your virtual environment:

    source ./venv/bin/activate

### Launching design patters 

  - Abstract Factory

         cd creational/abstract_factory
         python app.py --type=1
         python app.py --type=2

  - Builder

         cd creational/builder
         python app.py

  - Factory Method

         cd creational/factory_method
         python app.py -t=a
         python app.py -t=b

  - Prototype

         cd creational/prototype
         python app.py

  - Singleton

         cd creational/singleton
         python app.py

  - Adapter

         cd structural/adapter
         python app.py

  - Bridge

         cd structural/bridge
         python app.py -t=svg
         python app.py -t=canvas

  - Composite

         cd structural/composite
         python app.py
