// TaskModel holds the task data for the app, and creates an API for manipulating the tasks.

var TaskModel = function() {
    this.tasks = [];
    this.selectedTasks = [];
    this.addTaskEvent = new Event(this);
    this.deleteTaskEvent = new Event(this);
    this.setAsCompleteEvent = new Event(this);
}

TaskModel.prototype = {
    addTask: function(task) {
        this.tasks.push({
            taskName: task,
            taskStatus: 'uncompleted'
        });
    },

    getTasks: function() {
        return this.tasks;
    },

    setSelectedTask: function(taskIndex) {
        this.selectedTasks.push(taskIndex);
    },

    unselectTask: function(taskIndex) {
        this.selectedTasks.splice(taskIndex, 1);
    },

    setTasksAsCompleted: function() {
        var selectedTasks = this.selectedTasks;
        for(var index in selectedTasks) {
            this.tasks[selectedTasks[index]].taskStatus = 'completed';
        }
        this.selectedTasks = [];
        this.setAsCompleteEvent.notify();
    },

    deleteTasks: function() {
        var selectedTasks = this.selectedTasks;
        for(var index in selectedTasks) {
            this.tasks.splice(selectedTasks[index],1);
        }
        this.selectedTasks = [];
        this.deleteTaskEvent.notify();
    }
}