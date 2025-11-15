<script lang="ts">
export const description = "Teacher messaging page"
export const iframeHeight = "800px"
export const containerClass = "w-full h-full"
</script>

<script setup lang="ts">
import { ref, computed, nextTick } from "vue"

import AppSidebar from "@/components/sidebars/AppSidebar.vue"
import {
  SidebarProvider,
  SidebarInset,
  SidebarTrigger,
} from "@/components/ui/sidebar"

import {
  Breadcrumb,
  BreadcrumbList,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"

import { Separator } from "@/components/ui/separator"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"

import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"

import { MessageSquare, SendHorizontal, User, Search } from "lucide-vue-next"

const userRole = "Teacher"

// Dummy chat users
const conversations = ref([
  {
    id: 1,
    name: "Samantha Cruz",
    section: "STEM 11 - A",
    lastMessage: "Thank you po sir!",
  },
  {
    id: 2,
    name: "Joshua Ramirez",
    section: "ABM 12 - A",
    lastMessage: "Pwede po ba magpahabol?",
  },
  {
    id: 3,
    name: "Marjorie Tan",
    section: "HUMSS 12 - B",
    lastMessage: "Noted po.",
  },
])

// Chat history per user
const chatMessages = ref({
  1: [
    { from: "student", text: "Good morning sir!" },
    { from: "teacher", text: "Good morning! How can I help you?" },
    { from: "student", text: "Ask ko lang po yung instructions kanina." },
  ],
  2: [
    { from: "student", text: "Pwede po ba magpahabol ng assignment?" },
  ],
  3: [
    { from: "student", text: "Thank you po!" },
    { from: "teacher", text: "You're welcome!" },
  ],
})

const selectedChat = ref(1)
const searchQuery = ref("")
const messageText = ref("")

const filteredConversations = computed(() => {
  return conversations.value.filter((c) =>
    c.name.toLowerCase().includes(searchQuery.value.toLowerCase())
  )
})

function selectChat(id: number) {
  selectedChat.value = id
  nextTick(() => scrollToBottom())
}

function sendMessage() {
  if (!messageText.value.trim()) return

  chatMessages.value[selectedChat.value].push({
    from: "teacher",
    text: messageText.value,
  })

  messageText.value = ""
  nextTick(() => scrollToBottom())
}

function scrollToBottom() {
  const el = document.getElementById("chat-body")
  if (el) el.scrollTop = el.scrollHeight
}
</script>

<template>
  <SidebarProvider>
    <AppSidebar :userRole="userRole" />

    <SidebarInset>
      <!-- Header -->
      <header class="flex h-16 shrink-0 items-center gap-2 px-4">
        <SidebarTrigger class="-ml-1" />
        <Separator orientation="vertical" class="mx-2 h-4" />

        <Breadcrumb>
          <BreadcrumbList>
            <BreadcrumbItem>
              <BreadcrumbLink href="/teacher/dashboard">Teacher</BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator />
            <BreadcrumbItem>
              <BreadcrumbPage>Messages</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>

      <!-- MAIN CONTENT -->
      <div class="flex flex-1 flex-col p-4 pt-0 gap-4">
        <h2 class="text-2xl font-bold tracking-tight">Messages</h2>
        <p class="text-sm text-muted-foreground">
          Chat with your students for updates and clarifications.
        </p>

        <Card class="flex flex-1 overflow-hidden">
          <CardContent class="p-0 flex flex-1 overflow-hidden">
            <!-- LEFT COLUMN — USER LIST -->
            <div class="w-full md:w-1/3 border-r flex flex-col">
              <div class="p-4 border-b">
                <div class="relative">
                  <Search class="absolute left-2 top-1/2 -translate-y-1/2 h-4 w-4 text-muted-foreground" />
                  <Input
                    class="pl-8"
                    placeholder="Search students..."
                    v-model="searchQuery"
                  />
                </div>
              </div>

              <div class="flex-1 overflow-y-auto">
                <div
                  v-for="c in filteredConversations"
                  :key="c.id"
                  class="p-4 flex items-center gap-3 border-b cursor-pointer hover:bg-muted/50"
                  :class="{ 'bg-muted/40': c.id === selectedChat }"
                  @click="selectChat(c.id)"
                >
                  <User class="h-8 w-8 rounded-full bg-muted p-1" />
                  <div class="flex flex-col">
                    <p class="font-semibold">{{ c.name }}</p>
                    <p class="text-xs text-muted-foreground">
                      {{ c.lastMessage }}
                    </p>
                  </div>
                </div>
              </div>
            </div>

            <!-- RIGHT COLUMN — CHAT WINDOW -->
            <div class="flex-1 flex flex-col">
              <div class="p-4 border-b flex items-center gap-3">
                <User class="h-8 w-8 rounded-full bg-muted p-1" />
                <div>
                  <p class="font-semibold">
                    {{
                      conversations.find((x) => x.id === selectedChat)?.name
                    }}
                  </p>
                  <p class="text-xs text-muted-foreground">
                    {{
                      conversations.find((x) => x.id === selectedChat)?.section
                    }}
                  </p>
                </div>
              </div>

              <!-- CHAT BODY -->
              <div
                id="chat-body"
                class="flex-1 overflow-y-auto p-4 space-y-3 bg-muted/10"
              >
                <div
                  v-for="(msg, index) in chatMessages[selectedChat]"
                  :key="index"
                  class="flex"
                  :class="{
                    'justify-end': msg.from === 'teacher',
                    'justify-start': msg.from === 'student'
                  }"
                >
                  <div
                    class="rounded-xl px-4 py-2 max-w-xs"
                    :class="{
                      'bg-primary text-primary-foreground':
                        msg.from === 'teacher',
                      'bg-white border':
                        msg.from === 'student'
                    }"
                  >
                    {{ msg.text }}
                  </div>
                </div>
              </div>

              <!-- MESSAGE INPUT -->
              <div class="p-4 border-t flex gap-2">
                <Input
                  placeholder="Type your message..."
                  v-model="messageText"
                  @keyup.enter="sendMessage"
                />
                <Button class="gap-1" @click="sendMessage">
                  <SendHorizontal class="h-4 w-4" />
                  Send
                </Button>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
