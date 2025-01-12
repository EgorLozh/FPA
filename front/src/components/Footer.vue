<template>
    <footer class="footer">
        <p>&copy; 2024 ScriptTracker</p>
    </footer>
</template>

<script>
export default {
    name: 'Footer'
}
</script>

<style scoped>
.footer {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 60px;
    background-color: #f8f9fa;
    border-top: 1px solid #e7e7e7;
}

.footer p {
    margin: 0;
    font-size: 14px;
    color: #6c757d;
}
</style>