
# In Care (React Flask)
A web application for creating and maintaining Patient Records and Prescriptions for each of the registered patients. The intended users of this app will be Doctors/ Health care providers to manage Electronic Health Records of Patients . 



## Documentation

[Documentation](https://linktodocumentation)


## API Reference

#### POST User Login

```http GET
  /api/login
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.

