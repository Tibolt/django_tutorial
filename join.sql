SELECT auth_user.id as user_id, polls_user.name 
FROM auth_user
JOIN polls_user
ON auth_user.username = polls_user.username;
