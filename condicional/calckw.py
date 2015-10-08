print('---------------')
print('  CALCULADORA  ')
print(' CONTA ENERGIA ')
print('---------------\n\n')

valor_kw = float(input('Valor kw    : '))
kw_consumido = float(input('Kw consumido: '))
tx_imposto = float(input('% de imposto: '))

subtotal = valor_kw * kw_consumido

if subtotal < 10:
    subtotal = 10

imposto = subtotal * tx_imposto
total = subtotal + imposto

print('\nSubtotal = R$%8.2f' % subtotal)
print('Imposto  = R$%8.2f' % imposto)
print('Total    = R$%8.2f' % total)
