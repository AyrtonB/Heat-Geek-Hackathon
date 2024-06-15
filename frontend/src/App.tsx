import { Layout, Space } from 'antd'
import React from 'react'
import AddressSearch from './components/address-search';
import HeatpumpSetup from './components/heatpump-setup';
import AnnualSavings from './components/annual-savings';

const App:React.FC = () => {
  return (
    <Layout>
      <Space direction='vertical' style={{ padding: 24 }}>
        <AddressSearch />
        <HeatpumpSetup /> 
        <AnnualSavings/>
      </Space>
    </Layout>
  )
}

export default App;