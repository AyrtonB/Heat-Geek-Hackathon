import { Layout, Space } from 'antd'
import React from 'react'
import AddressSearch from './components/address-search';
import HeatpumpSetup from './components/heatpump-setup';
import CurrentProperty from './components/current-property';

const App:React.FC = () => {
  return (
    <Layout>
      <Space direction='vertical' style={{ padding: 24 }}>
        <AddressSearch />
        <HeatpumpSetup /> 
      </Space>
    </Layout>
  )
}

export default App;