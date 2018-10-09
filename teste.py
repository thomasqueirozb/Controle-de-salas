# with open('salas.txt','r') as s:
#     d=s.readlines()
#     d=[i.replace('\n','') for i in d]
# # d=['201', '202', '203', '204', '205', '206', '302', '308', '405', '406', '407', '408', '410', 'AUDITÓRIO STEFFI E MAX PERLMAN', 'BM&F BOVESPA 1', 'BM&F BOVESPA 2', 'EUGÊNIO GUDIN', 'MARCOS LOPES', 'MARIO HABERFELD', 'OCTAVIO GOUVEA DE BULHÕES', 'PAULO RENATO DE SOUZA', 'PETER DRUCKERROBERTO SIMONSEN', 'ROBERTO SIMONSEN', 'SEBASTIÃO CAMARGO', 'SOUZA DANTAS', 'VICENTE FALCONI CAMPOS']
#
# with open('salas.txt','w') as s:
#
#     new = sorted(list(set(d)))
#     s.write('\n'.join(new))
#     # d=[i.replace('\n','') for i in d]
# # print(sorted(list(set(d))))


a = '''SALAS AQUI'''

a=a.split('\n')
a=list(set(a))
# print(a)

with open('salas.txt','r') as s:
    d=s.readlines()
    d=[i.replace('\n','') for i in d]
# d=['201', '202', '203', '204', '205', '206', '302', '308', '405', '406', '407', '408', '410', 'AUDITÓRIO STEFFI E MAX PERLMAN', 'BM&F BOVESPA 1', 'BM&F BOVESPA 2', 'EUGÊNIO GUDIN', 'MARCOS LOPES', 'MARIO HABERFELD', 'OCTAVIO GOUVEA DE BULHÕES', 'PAULO RENATO DE SOUZA', 'PETER DRUCKERROBERTO SIMONSEN', 'ROBERTO SIMONSEN', 'SEBASTIÃO CAMARGO', 'SOUZA DANTAS', 'VICENTE FALCONI CAMPOS']

for i in a:
    if i not in d:
        d.append(i)

with open('salas.txt','w') as s:

    new = sorted(list(set(d)))
    s.write('\n'.join(new))
    # d=[i.replace('\n','') for i in d]
# print(sorted(list(set(d))))
