import React from 'react'
import logo from './logo.png'

const Logo = () => {
  return (
    <div class="flex flex-row justify-center p-3">
        <img src={logo} alt="logo" width={150} height={50} />
    </div>
  )
}

export default Logo