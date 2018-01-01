import click
from pymongo import MongoClient

@click.group()
@click.pass_context
def cli(ctx):
    client = MongoClient('localhost',27017);
    db = client.reconmaster
    ctx.obj['CONN'] = db  

@cli.group()
@click.pass_context
def config(ctx):
    click.echo('Se está corriendo la configuración')

@config.command()
@click.pass_context
@click.option("-key",type=click.STRING)
@click.option("-value",type=click.STRING)
def add(ctx,key,value):
    db = ctx.obj['CONN']
    col_config = db.config
    config_val = col_config.find({"key":key})
    if (config_val.count() > 0):
        click.echo("Ya existe valor para la key: " + key)
    else:    
        col_config.insert_one({"key":key,"value":value})
    click.echo("Se ejecuto correctamente")

@config.command()
@click.pass_context
@click.option("-key",type=click.STRING)
def delete(ctx,key):
    db = ctx.obj['CONN']
    col_config = db.config
    col_config.delete_one({"key":key})

@config.command()
@click.pass_context
@click.option("-key",type=click.STRING)
@click.option("-value",type=click.STRING)
def update(ctx, key,value):
    db = ctx.obj['CONN']
    col_config = db.config
    config_val = col_config.find({"key":key})
    if (config_val.count() == 0):
        click.echo("No existe valor para la key: " + key)
    else:    
        col_config.update_one({"key":key}, {"$set": {"value":value}}, upsert=False)
    
@config.command()
@click.pass_context
@click.option("--print-all","-a", is_flag=True)
@click.option("-key", default="", type=click.STRING)
def show(ctx, print_all, key):
    db = ctx.obj['CONN']
    col_config = db.config
    if (print_all):
        for config_val in col_config.find():
            click.echo(config_val['key'] + " = " + config_val['value'])
    else:
        config_val = col_config.find({"key":key})
        if (config_val.count() == 0):
            click.echo("No existe valor para la key: " + key)
        else:
             click.echo(key + " = " + config_val[0]['value'])
    
@cli.command()
@click.pass_context
@click.option('--count', default=1, help='number of greetings')
def dropdb(ctx):
    click.echo('Dropped the database')


cli.add_command(config)
config.add_command(add)
config.add_command(delete)
config.add_command(update)
config.add_command(show)
cli.add_command(dropdb)

if __name__ == '__main__':
    
    #cli(obj={})