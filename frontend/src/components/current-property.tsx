import { Alert } from 'antd'
import React from 'react'
import { useSelector } from 'react-redux'
import { RootState } from '../state'

const CurrentProperty: React.FC = () => {
    const name = useSelector((r: RootState) => r.property.addressLookup?.home?.address)
    if(!name) return null
    return (
        <Alert message={`Found: ${name}`} type="info" />
    )
}

export default CurrentProperty