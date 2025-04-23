#!/usr/bin/env python

"""
This is a module that can perform calculations like addition, subtraction,
multiplication, and division.
This module can also be invoked from the command line script using click.
"""

import click 

def add(x, y):
    """Add two numbers."""
    return x + y

def subtract(x, y):
    """Subtract two numbers."""
    return x - y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def divide(x, y):   
    """Divide two numbers."""
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

#build a click group
@click.group()
def cli():
    """Simple calculator."""
    pass
#add a command to the group 

@cli.command("add")
@click.argument('x', type=float)
@click.argument('y', type=float)
def add_command(x, y):
    """Add two numbers."""
    result = add(x, y)
    click.echo(click.style(f"{x} + {y} = {result}", fg="green", bold=True))

@cli.command("subtract")
@click.argument('x', type=float)   
@click.argument('y', type=float)
def subtract_command(x, y):
    """Subtract two numbers."""
    result = subtract(x, y)
    click.echo(f"{x} - {y} = {result}")

@cli.command("multiply")
@click.argument('x', type=float)
@click.argument('y', type=float)
def multiply_command(x, y):
    """Multiply two numbers."""
    result = multiply(x, y)
    click.echo(f"{x} * {y} = {result}")

@cli.command("divide")
@click.argument('x', type=float)
@click.argument('y', type=float)
def divide_command(x, y):
    """Divide two numbers."""
    try:
        result = divide(x, y)
        click.echo(f"{x} / {y} = {result}")
    except ValueError as e:
        click.echo(e)

if __name__ == '__main__':
    cli()
# This code is a simple calculator that can perform addition, subtraction,
# multiplication, and division.