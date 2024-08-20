import React, { useState } from "react";

const Signup = () => {
  const [formData, setFormData] = useState({
    first_name: "",
    last_name: "",
    email: "",
    password: "",
  });

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  }

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await fetch("http://localhost:5000/customers/add", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });
      if (response.ok) {
        alert("Account created successfully!");
      } else {
        alert("Account creation failed!");
      }
    } catch (error) {
      console.log("Error occurred!");
      console.error(error);
    }
  }
  
  return (
    <div>
      <div className="flex flex-col justify-center items-center w-screen my-20">
        <form onSubmit={handleSubmit} className="border-2 border-orange-400 shadow-md rounded-2xl px-8 pt-6 pb-3">
          <div class="form-item my-2">
            <label for="firs_name" className="font-medium">First name: </label>
            <br />
            <input
              type="text"
              name="first_name"
              value={formData.first_name}
              onChange={handleChange}
              required
              className="bg-orange-100 rounded-md p-1"
            />
          </div>
          <div class="form-item my-2">
            <label for="last_name" className="font-medium">Last name: </label>
            <br />
            <input
              type="text"
              name="last_name"
              value={formData.last_name}
              onChange={handleChange}
              required
              className="bg-orange-100 rounded-md p-1"
            />
          </div>
          <div class="form-item my-2">
            <label for="email" className="font-medium">Email: </label>
            <br />
            <input
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              required
              className="bg-orange-100 rounded-md p-1"
            />
          </div>
          <div class="form-item my-2">
            <label for="password" className="font-medium">Password: </label>
            <br />
            <input
              type="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              required
              className="bg-orange-100 rounded-md p-1"
            />
            </div>
            <div button className="float-right">
              <button
                type="submit"
                className="bg-orange-500 text-white p-2 rounded-md mt-4"
              >
                Sign Up
              </button>
            </div>
        </form>
      </div>
    </div>
  );
};

export default Signup;
