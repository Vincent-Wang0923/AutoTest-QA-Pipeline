import React from 'react';
import{BrowserRouter as Router,Routes,Route,useNavigate}from 'react-router-dom';
import{Form,Input,Button,Card,message,ConfigProvider}from 'antd';
import axios from 'axios';

const Login=()=>{
  const navigate=useNavigate();
  const onFinish=async(values)=>{
    try{
      const res=await axios.post('http://localhost:5000/api/login',values);
      message.success(res.data.message);
    }catch(error){
      message.error(error.response?.data?.message||'Login failed');
    }
  };
  return(
    <div style={{display:'flex',justifyContent:'center',marginTop:'100px'}}>
      <Card title="Login" style={{width:350,boxShadow:'0 4px 12px rgba(0,0,0,0.1)'}}>
        <Form onFinish={onFinish} layout="vertical">
          <Form.Item label="Username" name="username" rules={[{required:true,message:'Username required'}]}>
            <Input placeholder="Enter username"/>
          </Form.Item>
          <Form.Item label="Password" name="password" rules={[{required:true,message:'Password required'}]}>
            <Input.Password placeholder="Enter password"/>
          </Form.Item>
          <Button type="primary" htmlType="submit" block>Login</Button>
          <div style={{marginTop:'15px',textAlign:'center'}}>
            <Button type="link" onClick={()=>navigate('/register')}>Need an account? Register</Button>
          </div>
        </Form>
      </Card>
    </div>
  );
};

const Register=()=>{
  const navigate=useNavigate();
  const onFinish=async(values)=>{
    try{
      //Pre-planted bug
      const res=await axios.post('http://localhost:5000/api/register',values);
      message.success(res.data.message);
      navigate('/');
    }catch(error){
      message.error(error.response?.data?.message||'Registration failed');
    }
  };
  return(
    <div style={{display:'flex',justifyContent:'center',marginTop:'100px'}}>
      <Card title="Register" style={{width:350,boxShadow:'0 4px 12px rgba(0,0,0,0.1)'}}>
        <Form onFinish={onFinish} layout="vertical">
          <Form.Item label="Username" name="username" rules={[{required:true,message:'Username required'}]}>
            <Input placeholder="Set username"/>
          </Form.Item>
          <Form.Item label="Password" name="password" rules={[{required:true,message:'Password required'}]}>
            <Input.Password placeholder="Set password"/>
          </Form.Item>
          <Button type="primary" htmlType="submit" block>Register</Button>
          <div style={{marginTop:'15px',textAlign:'center'}}>
            <Button type="link" onClick={()=>navigate('/')}>Have an account? Login</Button>
          </div>
        </Form>
      </Card>
    </div>
  );
};

const App=()=>(
  <ConfigProvider theme={{token:{colorPrimary:'#722ed1'}}}>
    <Router>
      <Routes>
        <Route path="/" element={<Login/>}/>
        <Route path="/register" element={<Register/>}/>
      </Routes>
    </Router>
  </ConfigProvider>
);

export default App;