# Base Plan
## Model
```
User
    email
    full_name
    phone
    is_admin
```


```
Donation
    user --> FK (User)
    category
    amount
    status
    payment_id
    transaction_id
```

```
Event
    user --> FK (User)
    name
    description
    purpose
    event_date
    is_approved
```

## Routes
### Users
```
# Login 
/users/login

# Register
/users/register

# Logout
/users/Logout

# Profile
/users/profile

# Password Reset
/users/password_reset

```
### Home
```
/
/contact_us
/about_us
```

### Donations
```
Previous Donations List
/donations/

New Donation
/donations/new

Donation payment_id
/donations/:id/payment

Donation Detail
/donations/:id/detail
```

### Events
```
Events List
/events/

New Event Request
/events/new

Event Detail
/events/:id/detail
```