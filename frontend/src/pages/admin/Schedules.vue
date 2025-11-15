<script lang="ts">
export const description = "Schedules management page"
export const iframeHeight = "800px"
export const containerClass = "w-full h-full"
</script>

<script setup lang="ts">
import { ref } from "vue"

import AppSidebar from "@/components/sidebars/AppSidebar.vue"
import {
  SidebarProvider,
  SidebarInset,
  SidebarTrigger,
} from "@/components/ui/sidebar"

import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbList,
  BreadcrumbLink,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"

import { Separator } from "@/components/ui/separator"

import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
} from "@/components/ui/card"

import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"

import {
  Table,
  TableHeader,
  TableRow,
  TableHead,
  TableBody,
  TableCell,
} from "@/components/ui/table"

import {
  DropdownMenu,
  DropdownMenuTrigger,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
} from "@/components/ui/dropdown-menu"

import {
  Plus,
  MoreHorizontal,
  Calendar,
  Clock,
  MapPin,
} from "lucide-vue-next"

const userRole = "Admin"

// Dummy schedules data
const schedules = ref([
  {
    id: 1,
    subject: "General Mathematics",
    section: "Grade 11 – STEM A",
    teacher: "Maria Santos",
    day: "Monday",
    time: "8:00 AM – 9:30 AM",
    room: "Room 201",
    color: "bg-blue-500",
  },
  {
    id: 2,
    subject: "Oral Communication",
    section: "Grade 11 – HUMSS B",
    teacher: "Juan Dela Cruz",
    day: "Tuesday",
    time: "10:00 AM – 11:30 AM",
    room: "Room 105",
    color: "bg-green-500",
  },
  {
    id: 3,
    subject: "Accountancy Fundamentals",
    section: "Grade 12 – ABM A",
    teacher: "Ana Reyes",
    day: "Wednesday",
    time: "1:00 PM – 2:30 PM",
    room: "Room 310",
    color: "bg-yellow-500",
  },
  {
    id: 4,
    subject: "Physical Education 2",
    section: "Grade 12 – GAS C",
    teacher: "Robert Garcia",
    day: "Friday",
    time: "3:00 PM – 4:30 PM",
    room: "Gymnasium",
    color: "bg-red-500",
  },
])

const search = ref("")
</script>

<template>
  <SidebarProvider>
    <AppSidebar :userRole="userRole" />

    <SidebarInset>
      <!-- Header -->
      <header class="flex h-16 shrink-0 items-center gap-2 px-4 transition-all">
        <SidebarTrigger class="-ml-2" />
        <Separator orientation="vertical" class="mx-2 h-4" />

        <Breadcrumb>
          <BreadcrumbList>
            <BreadcrumbItem>
              <BreadcrumbLink href="/admin/dashboard">Admin</BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator />
            <BreadcrumbItem>
              <BreadcrumbPage>Schedules</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>

      <!-- Content -->
      <div class="flex flex-1 flex-col gap-4 p-4 pt-0">

        <!-- Top Bar -->
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-2xl font-bold tracking-tight">Schedules</h2>
            <p class="text-sm text-muted-foreground">
              Manage class schedules, teachers, and assigned rooms.
            </p>
          </div>

          <Button class="flex items-center gap-2">
            <Plus class="h-4 w-4" />
            Add Schedule
          </Button>
        </div>

        <Card>
          <CardHeader>
            <CardTitle>Schedules Overview</CardTitle>
            <CardDescription>
              View, edit, or adjust class schedules.
            </CardDescription>
          </CardHeader>

          <CardContent>
            <!-- Search -->
            <div class="flex items-center justify-between mb-4">
              <Input
                v-model="search"
                placeholder="Search schedules..."
                class="max-w-xs"
              />
            </div>

            <!-- Table -->
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead class="w-56">Subject</TableHead>
                  <TableHead>Section</TableHead>
                  <TableHead>Teacher</TableHead>
                  <TableHead>Schedule</TableHead>
                  <TableHead>Room</TableHead>
                  <TableHead class="text-right w-20">Actions</TableHead>
                </TableRow>
              </TableHeader>

              <TableBody>
                <TableRow
                  v-for="sc in schedules"
                  :key="sc.id"
                  class="hover:bg-muted/50"
                >
                  <!-- Subject -->
                  <TableCell>
                    <div class="flex items-center gap-2">
                      <div
                        class="h-3 w-3 rounded-full"
                        :class="sc.color"
                      ></div>
                      <p class="font-medium">{{ sc.subject }}</p>
                    </div>
                  </TableCell>

                  <!-- Section -->
                  <TableCell class="text-muted-foreground">
                    {{ sc.section }}
                  </TableCell>

                  <!-- Teacher -->
                  <TableCell class="text-muted-foreground">
                    {{ sc.teacher }}
                  </TableCell>

                  <!-- Schedule -->
                  <TableCell>
                    <div class="flex flex-col text-sm">
                      <div class="flex items-center gap-1">
                        <Calendar class="h-3 w-3" />
                        <span>{{ sc.day }}</span>
                      </div>
                      <div class="flex items-center gap-1 text-muted-foreground">
                        <Clock class="h-3 w-3" />
                        <span>{{ sc.time }}</span>
                      </div>
                    </div>
                  </TableCell>

                  <!-- Room -->
                  <TableCell>
                    <div class="flex items-center gap-1">
                      <MapPin class="h-3 w-3 text-muted-foreground" />
                      <span>{{ sc.room }}</span>
                    </div>
                  </TableCell>

                  <!-- Actions -->
                  <TableCell class="text-right">
                    <DropdownMenu>
                      <DropdownMenuTrigger as-child>
                        <Button variant="ghost" size="icon">
                          <MoreHorizontal class="h-4 w-4" />
                        </Button>
                      </DropdownMenuTrigger>

                      <DropdownMenuContent align="end">
                        <DropdownMenuLabel>Actions</DropdownMenuLabel>
                        <DropdownMenuSeparator />

                        <DropdownMenuItem>Edit Schedule</DropdownMenuItem>
                        <DropdownMenuItem>Change Room</DropdownMenuItem>
                        <DropdownMenuItem>Assign Teacher</DropdownMenuItem>

                        <DropdownMenuSeparator />

                        <DropdownMenuItem class="text-red-600">
                          Delete Schedule
                        </DropdownMenuItem>
                      </DropdownMenuContent>
                    </DropdownMenu>
                  </TableCell>
                </TableRow>
              </TableBody>
            </Table>
          </CardContent>
        </Card>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
