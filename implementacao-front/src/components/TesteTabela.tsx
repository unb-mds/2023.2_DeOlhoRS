import { DataTable } from 'primereact/datatable'
import { Column } from 'primereact/column'
import 'primereact/resources/themes/lara-light-indigo/theme.css'
import 'primereact/resources/primereact.min.css'

import { useState } from 'react'
import { FilterMatchMode } from 'primereact/api'
import { InputText } from 'primereact/inputtext'

function TesteTabela() {

    const [filter, setFilter] = useState()

    const data = [
        {
            nome: 'Cleiton Rasta Robson',
            cpf: '000.000.000-00',
            cargo: 'Analista de Processos',
            acao: 'Nomeação',
            dia: '25/09/2003',
        },
        {
            nome: 'Cleiton Robson Rastah',
            cpf: '000.000.000-01',
            cargo: 'Analista financeiro',
            acao: 'Nomeação',
            dia: "25/09/2007",
        },
        {
            nome: 'Cleiton Arrasta',
            cpf: '000.000.000-02',
            cargo: 'Analista de Processos',
            acao: 'Exoneração',
            dia: '25/09/2010'
        }
    ]


  return (
    <div>
        <input type="text" name="nome" id="nome" />
        <input type="submit" value="Buscar"/>

        <DataTable value={data} filters={filter}>
            <Column field='nome' header='Nome' />
            <Column field='cpf' header='CPF' />
            <Column field='cargo' header='Cargo' />
            <Column field='acao' header='Ação' />
            <Column field='dia' header='Data' />
        </DataTable>
    </div>
  )
}

export default TesteTabela
