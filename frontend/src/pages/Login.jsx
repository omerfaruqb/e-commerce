import React from "react";

const Login = () => {
  return (
    <div>
      <div className="flex flex-col justify-center items-center w-screen my-20">
        <form className="border-2 border-orange-400 shadow-md rounded-2xl px-8 pt-6 pb-3">
          <div class="form-item my-2">
            <label for="email" className="font-medium">Email: </label>
            <br />
            <input
              type="email"
              id="email"
              name="email"
              required
              className="bg-orange-100 rounded-md p-1"
            />
          </div>
          <div class="form-item my-2">
            <label for="password" className="font-medium">Password: </label>
            <br />
            <input
              type="password"
              id="password"
              name="password"
              required
              className="bg-orange-100 rounded-md p-1"
            />
            </div>
            <div button className="float-right">
              <button
                type="submit"
                className="bg-orange-500 text-white p-2 rounded-md mt-4"
              >
                Login
              </button>
            </div>
        </form>
      </div>
    </div>
  );
};

export default Login;
