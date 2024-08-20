import React from 'react'
import Button from './Button'

const Accounts = () => {
  return (
    <div className='flex flex-row justify-between m-4'>
      <Button buttonName="Log In" buttonUrl="/login" />
      <Button buttonName="Sign Up" buttonUrl="/signup" />
    </div>
  )
}

export default Accounts