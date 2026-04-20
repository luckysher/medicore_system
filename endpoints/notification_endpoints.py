
@app.post("/notification/mark/read/{note_id}", status_code=status.HTTP_200_OK, tags=[Tags.notification])
async def mark_notification_as_read(note_id:int, session: SessionDep, user: Annotated[User, Depends(is_authenticated)]):
    pass
