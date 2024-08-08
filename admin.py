from fastapi import FastAPI
from sqlmodel import SQLModel, Field, create_engine
from sqladmin import Admin, ModelView

# Define your SQLModel models
class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    password: str

class Item(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str

# Create a database engine
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, echo=True)

# Create the FastAPI app
app = FastAPI()

# Initialize the database
@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

# Set up SQLAdmin
class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username]

class ItemAdmin(ModelView, model=Item):
    column_list = [Item.id, Item.name]

admin = Admin(app, engine)
admin.add_view(UserAdmin)
admin.add_view(ItemAdmin)

# Now you can run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
